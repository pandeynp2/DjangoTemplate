import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import Home from "../Home"; // Adjust the path based on your file structure

describe("Home Component", () => {
  test("renders the home page content", () => {
    render(<Home />);

    // Check if the main heading is rendered
    const heading = screen.getByText(/hello, world!/i);
    expect(heading).toBeInTheDocument();

    // Check if the paragraph is rendered
    const paragraph = screen.getByText(
      /welcome to the home page of our simple react application\./i
    );
    expect(paragraph).toBeInTheDocument();

    // Check if all buttons are rendered
    const aboutButton = screen.getByText(/about us/i);
    const servicesButton = screen.getByText(/services/i);
    const contactButton = screen.getByText(/contact us/i);

    expect(aboutButton).toBeInTheDocument();
    expect(servicesButton).toBeInTheDocument();
    expect(contactButton).toBeInTheDocument();
  });

});
