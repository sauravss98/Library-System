import { React, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import "../Home/Home.css";
import BookListContainer from "../BookListContainer/BookListContainer";
import axiosInstance from "../../utils/Axios";

const Home = () => {
  const [books, setBooks] = useState([]);
  const navigate = useNavigate();
  useEffect(() => {
    const fetchData = async () => {
      try {
        let token;
        const tokenString = localStorage.getItem("user_data");
        if (tokenString) {
          const tokenConverted = JSON.parse(tokenString);
          token = tokenConverted.token;
        }
        let authToken = {
          Authorization: "Token " + token,
        };
        const response = await axiosInstance.get("books/list/", {
          headers: {
            authToken,
          },
        });
        setBooks(response.data);
      } catch (error) {
        if (error.response.status === 403) {
          navigate("/");
        }
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <Container>
        <Row>
          {books.map((book) => (
            <BookListContainer key={book.id} product={book} />
          ))}
        </Row>
      </Container>
    </div>
  );
};

export default Home;
