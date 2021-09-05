import React, { createContext, useEffect, useState } from 'react';
import { getUser, logout } from '../services/userService';

const AppContext = createContext();

export function ContextProvider({ children }) {
  const [user, setUser] = useState({});

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
  }, []);
  return (
    <AppContext.Provider
      value={{
        user: user,
        userLogout: userLogout,
        atualizarUser: atualizarUser,
      }}
    >
      {children}
    </AppContext.Provider>
  );
}

export default AppContext;
