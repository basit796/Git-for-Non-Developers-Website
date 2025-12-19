import React from 'react';
import GitChatbot from '../components/GitChatbot';

/**
 * Root component wrapper for Docusaurus
 * This component wraps all pages and adds the chatbot globally
 */
export default function Root({ children }) {
  return (
    <>
      {children}
      <GitChatbot />
    </>
  );
}
