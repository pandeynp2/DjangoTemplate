import React from "react";
import { render, screen } from "@testing-library/react";
import Button from "../Button"; // Update the path to your component

describe("Button Component", () => {
  test("renders the button with the given label", () => {
    render(<Button label="Click Me" onClick={() => {}} />);
    const buttonElement = screen.getByText(/Click Me/i);
    expect(buttonElement).toBeInTheDocument();
  });
});
