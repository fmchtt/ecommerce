import React, { createContext, useEffect, useState } from 'react';
import { getCategories } from '../services/categoryService';
import { getUser, logout } from '../services/userService';

const AppContext = createContext();

export function ContextProvider({ children }) {
  const [user, setUser] = useState({});
  const [categories, setCategories] = useState([]);

  function userLogout() {
    logout()
      .then(() => {
        setUser({});
      })
      .catch(() => {});
  }

  function atualizarUser() {
    getUser()
      .then(response => {
        setUser(response.data);
      })
      .catch(() => {});
  }

  useEffect(() => {
    atualizarUser();
    getCategories().then(response => {
      setCategories(response.data);
    });
  }, []);
  return (
    <AppContext.Provider
      value={{
        user: user,
        userLogout: userLogout,
        atualizarUser: atualizarUser,
        categories: categories,
      }}
    >
      {children}
    </AppContext.Provider>
  );
}

export default AppContext;
