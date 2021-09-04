import axios from 'axios';

function getCookie() {
  const cookies = document.cookie.split(';');
  return cookies[0].split('=')[1];
}

export function getHeaders() {
  return getCookie() ? { 'X-CSRF-TOKEN': getCookie() } : {};
}

const http = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
  withCredentials: true,
});

export default http;
