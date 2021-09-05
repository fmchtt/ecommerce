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
  LinkBox,
} from '@chakra-ui/react';
import { FaChevronDown } from 'react-icons/fa';
import { AiOutlineShoppingCart } from 'react-icons/ai';
import userContext from './context/appContext';
import Login from './pages/Login';
import Home from './pages/Home';
import Showcase from './pages/Showcase';
import UserProducts from './pages/CreatedByUser';
import Register from './pages/Register';

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
        <Text as={rrd} to="/" fontSize="3xl">
          Ecommerce
        </Text>
        <Box d="flex" alignItems="center" gridGap={5}>
          {user.id ? (
            <>
              <LinkBox
                as={rrd}
                bg="gray.100"
                p={2}
                borderRadius="base"
                _hover={{
                  backgroundColor: 'gray.200',
                }}
              >
                <AiOutlineShoppingCart size={25} />
              </LinkBox>
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
                  <MenuItem as={rrd} to="/products">
                    Meus produtos
                  </MenuItem>
                  <MenuItem onClick={userLogout}>Logout</MenuItem>
                </MenuList>
              </Menu>
            </>
          ) : (
            <>
              <Link fontSize="2xl" as={rrd} to="/login">
                Login
              </Link>
              <Link fontSize="2xl" as={rrd} to="/register">
                Registrar
              </Link>
            </>
          )}
        </Box>
      </Box>
      <Switch>
        <Route path="/products">
          <UserProducts />
        </Route>
        <Route path="/product/:id">
          <Showcase />
        </Route>
        <Route path="/register">
          <Register />
        </Route>
        <Route path="/login">
          <Login />
        </Route>
        <Route path="/">
          <Home />
        </Route>
      </Switch>
      <Box
        height="10vh"
        display="flex"
        justifyContent="space-between"
        alignItems="center"
        padding="6"
        bgColor="#f2f2f2"
      >
        <Text as={rrd} to="/" fontSize="3xl">
          Ecommerce
        </Text>
      </Box>
    </BrowserRouter>
  );
}

export default App;
