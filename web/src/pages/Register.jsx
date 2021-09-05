import React, { useState } from 'react';
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
import {
  FaUser as UserIcon,
  FaLock as LockIcon,
  FaUserMd,
} from 'react-icons/fa';
import { registrar } from '../services/userService';
import { useHistory } from 'react-router';

export default function Register() {
  const [errorAlert, setErrorAlert] = useState(null);

  const history = useHistory();

  function submitRegister(e) {
    e.preventDefault();
    registrar(new FormData(e.target))
      .then(a => {
        history.push('/login');
      })
      .catch(e => {
        setErrorAlert('Erro ao registrar');
      });
  }

  return (
    <Flex width="full" align="center" justifyContent="center" height="full">
      <Box borderWidth="1px" borderRadius="lg" p={6} m={20}>
        <Box textAlign="center">
          <Heading>Login</Heading>
        </Box>
        <Box my={4} textAlign="left">
          <form onSubmit={submitRegister}>
            <FormControl mt={6}>
              <FormLabel>Seu nome</FormLabel>
              <InputGroup>
                <InputLeftElement
                  pointerEvents="none"
                  children={<FaUserMd />}
                />
                <Input type="text" placeholder="Fulano Silva" name="username" />
              </InputGroup>
            </FormControl>
            <FormControl mt={6}>
              <FormLabel>Email</FormLabel>
              <InputGroup>
                <InputLeftElement
                  pointerEvents="none"
                  children={<UserIcon />}
                />
                <Input type="email" placeholder="test@test.com" name="email" />
              </InputGroup>
            </FormControl>
            <FormControl mt={6}>
              <FormLabel>Password</FormLabel>
              <InputGroup>
                <InputLeftElement
                  pointerEvents="none"
                  children={<LockIcon />}
                />
                <Input type="password" placeholder="*******" name="password" />
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
              Registrar
            </Button>
          </form>
        </Box>
      </Box>
    </Flex>
  );
}
