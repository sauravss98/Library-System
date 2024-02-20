import React, { useEffect, useState } from "react";
import "./BookListContainer.css";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import axiosInstance from "../../utils/Axios";
import { useNavigate } from "react-router-dom";

const BookListContainer = () => {
  const handleClick = async (book) => {
    console.log(book);
    let body = {
      book_ids:book.id,
    }
    const response = await axiosInstance.post("cart/cart-item/create",body);
    console.log(response)
  };

  const [books, setBooks] = useState([]);
  const navigate = useNavigate();
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axiosInstance.get("books/list/", {});
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
      {books.map((book) => (
        <Row key={book.id} className="main_container">
          <Col>
            <p>Book Title: {book.title}</p>
          </Col>
          <Col>
            <p>Author Name: {book.author_name}</p>
          </Col>
          <Col>
            <p>Quantity Left: {book.quantity}</p>
          </Col>
          <Col>
            <button onClick={() => handleClick(book)}>Add To Cart</button>
          </Col>
        </Row>
      ))}
    </div>
  );
};

export default BookListContainer;
