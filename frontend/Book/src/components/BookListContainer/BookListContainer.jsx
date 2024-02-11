import React, { useState } from "react";
import "./BookListContainer.css";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

const BookListContainer = (key, item) => {
  const [book, setBook] = useState([]);
  return (
    <div className="main_container">
      <Row>
        <Col>
          <text>Book Title: {}</text>
        </Col>
        <Col>
          <text>Author Name: {}</text>
        </Col>
        <Col>
          <text>Quantity Left: {}</text>
        </Col>
        <Col>
          <button>Add To Cart</button>
        </Col>
      </Row>
    </div>
  );
};

export default BookListContainer;
