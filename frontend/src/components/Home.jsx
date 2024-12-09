import React from 'react';

function Home() {
  return (
    <main className="home">
      <h2>Hello, World!</h2>
      <p>Welcome to the home page of our simple React application.</p>
      <div className="buttons">
        <button onClick={() => alert('Navigating to About Page...')}>About Us</button>
        <button onClick={() => alert('Navigating to Services Page...')}>Services</button>
        <button onClick={() => alert('Navigating to Contact Page...')}>Contact Us</button>
      </div>
    </main>
  );
}

export default Home;
