import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
//  esbuild: {
//    loader: 'jsx', // Enable JSX syntax in .js files
//    include: /src\/.*\.js$/, // Restrict JSX processing to .js files in the src folder
//  },
});
