import { React, useEffect, useState } from "react";

import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import "../Home/Home.css";
import BookListContainer from "../BookListContainer/BookListContainer";
import axiosInstance from "../../utils/Axios";

const Home = () => {
    return (
    <div>
      <Container>
        <Row>
          <BookListContainer />
        </Row>
      </Container>
    </div>
  );
};

export default Home;
