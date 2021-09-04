import React, { useContext, useState } from 'react';
import {
  Box,
  Input,
  InputLeftElement,
  InputGroup,
  FormControl,
  Flex,
  FormLabel,
  Button,
  Heading,
  Alert,
  AlertIcon,
  AlertTitle,
  CloseButton,
} from '@chakra-ui/react';
import { FaUser as UserIcon, FaLock as LockIcon } from 'react-icons/fa';
import context from '../context/appContext';
import { login } from '../services/userService';
import { useHistory } from 'react-router';

export default function Login() {
  const { atualizarUser } = useContext(context);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errorAlert, setErrorAlert] = useState(null);

  const history = useHistory();

  function submitLogin(e) {
    e.preventDefault();
    if (email && password) {
      login(email, password)
        .then(a => {
          atualizarUser();
          history.push('/');
        })
        .catch(e => {});
    } else {
      setErrorAlert('Usuario ou senha faltando!!');
    }
  }

  return (
    <Flex width="full" align="center" justifyContent="center" height="full">
      <Box p={2}>
        <Box textAlign="center">
          <Heading>Login</Heading>
        </Box>
        <Box my={4} textAlign="left">
          <form onSubmit={submitLogin}>
            <FormControl>
              <FormLabel>Email</FormLabel>
              <InputGroup>
                <InputLeftElement
                  pointerEvents="none"
                  children={<UserIcon />}
                />
                <Input
                  type="email"
                  placeholder="test@test.com"
                  onChange={e => {
                    setEmail(e.target.value);
                  }}
                />
              </InputGroup>
            </FormControl>
            <FormControl mt={6}>
              <FormLabel>Password</FormLabel>
              <InputGroup>
                <InputLeftElement
                  pointerEvents="none"
                  children={<LockIcon />}
                />
                <Input
                  type="password"
                  placeholder="*******"
                  onChange={e => {
                    setPassword(e.target.value);
                  }}
                />
              </InputGroup>
            </FormControl>
            {errorAlert ? (
              <Alert mt={6} status="error">
                <AlertIcon />
                <AlertTitle mr={2}>{errorAlert}</AlertTitle>
                <CloseButton
                  position="absolute"
                  right="8px"
                  top="8px"
                  onClick={() => {
                    setErrorAlert(null);
                  }}
                />
              </Alert>
            ) : null}
            <Button width="full" mt={4} type="submit">
              Entrar
            </Button>
          </form>
        </Box>
      </Box>
    </Flex>
  );
}
