export default {
  testEnvironment: "jsdom", // Required for DOM-based testing
  moduleNameMapper: {
    "\\.(css|less|scss|sass)$": "identity-obj-proxy" // Mock CSS imports
  },
  setupFilesAfterEnv: ["<rootDir>/jest.setup.js"], // Setup additional configurations
 transform: {
    "^.+\\.(js|jsx)$": "babel-jest", // Use Babel for .js and .jsx files
  },
  setupFilesAfterEnv: ["<rootDir>/jest.setup.js"], // Jest setup file
  moduleFileExtensions: ["js", "jsx"], // Recognize both .js and .jsx
};
