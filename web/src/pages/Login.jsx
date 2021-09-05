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
  const [errorAlert, setErrorAlert] = useState(null);
  const [loading, setLoading] = useState(false);

  const history = useHistory();

  function submitLogin(e) {
    e.preventDefault();
    setLoading(true);
    login(new FormData(e.target))
      .then(a => {
        atualizarUser();
        history.push('/');
        setLoading(false);
      })
      .catch(e => {
        setErrorAlert('Usuario ou senha incorreto!!');
        setLoading(false);
      });
  }

  return (
    <Flex width="full" align="center" justifyContent="center" height="full">
      <Box borderWidth="1px" borderRadius="lg" p={6} m={20}>
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
                <Input name="email" type="email" placeholder="test@test.com" />
              </InputGroup>
            </FormControl>
            <FormControl mt={6}>
              <FormLabel>Password</FormLabel>
              <InputGroup>
                <InputLeftElement
                  pointerEvents="none"
                  children={<LockIcon />}
                />
                <Input name="password" type="password" placeholder="*******" />
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
            <Button loadingText="Entrando..." isLoading={loading} width="full" mt={4} type="submit">
              Entrar
            </Button>
          </form>
        </Box>
      </Box>
    </Flex>
  );
}
