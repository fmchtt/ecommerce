import React, { useContext } from 'react';
import { BrowserRouter, Route, Switch, Link as rrd } from 'react-router-dom';
import {
  Box,
  Text,
  Link,
  Avatar,
  HStack,
  Menu,
  MenuButton,
  MenuList,
  Button,
  MenuItem,
} from '@chakra-ui/react';
import { FaChevronDown } from 'react-icons/fa';
import userContext from './context/appContext';
import Login from './pages/login';
import Home from './pages/home';

function App() {
  const { user, userLogout } = useContext(userContext);
  return (
    <BrowserRouter>
      <Box
        height="10vh"
        display="flex"
        justifyContent="space-between"
        alignItems="center"
        padding="6"
        bgColor="#f2f2f2"
      >
        <Text as={rrd} to="/" fontSize="3xl">Ecommerce</Text>
        <Box>
          {user.id ? (
            <Menu>
              <MenuButton as={Button} rightIcon={<FaChevronDown />}>
                <HStack>
                  <Avatar size="sm" src={user.avatar_url} />
                  <Text fontSize="2xl">{user.username}</Text>
                </HStack>
              </MenuButton>
              <MenuList>
                <MenuItem>Meu Perfil</MenuItem>
                <MenuItem>Meus Pedidos</MenuItem>
                <MenuItem>Meus produtos</MenuItem>
                <MenuItem>Criar Produto</MenuItem>
                <MenuItem onClick={userLogout}>Logout</MenuItem>
              </MenuList>
            </Menu>
          ) : (
            <Link fontSize="2xl" as={rrd} to="/login">
              Login
            </Link>
          )}
        </Box>
      </Box>
      <Switch>
        <Route path="/login">
          <Login />
        </Route>
        <Route path="/">
          <Home />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
