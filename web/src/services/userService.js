import http, { getHeaders } from '../configs/http';

export function getUser() {
  return http.get('users/me/');
}

export async function login(userName, password) {
  return http.post(
    'login',
    new URLSearchParams({ username: userName, password: password }),
    {
      headers: {
        'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
      },
    }
  );
}

export function logout() {
  return http.post(
    'logout/',
    {},
    {
      headers: getHeaders(),
    }
  );
}
