import http, { getHeaders } from '../configs/http';

export function getUser() {
  return http.get('users/me/');
}

export async function login(data) {
  return http.post('login', data, {
    headers: {
      'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    },
  });
}

export async function registrar(data) {
  return http.post('users/create/', data, {
    headers: {
      'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    },
  });
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
