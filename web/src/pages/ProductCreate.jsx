import React, { useState } from 'react';
import {
  Box,
  Center,
  FormControl,
  Input,
  FormLabel,
  Textarea,
  Button,
  useToast,
  Heading,
} from '@chakra-ui/react';
import { useHistory } from 'react-router-dom';
import { createProduct } from '../services/productService';

export default function ProductCreate() {
  const [loading, setLoading] = useState(false);
  const history = useHistory();
  const toast = useToast({
    title: 'Erro',
    description: 'Falha ao criar produto',
    status: 'error',
  });

  function submitCreate(e) {
    e.preventDefault();
    setLoading(true);
    createProduct(new FormData(e.target))
      .then(() => {
        setLoading(false);
        history.push('/products');
      })
      .catch(() => {
        setLoading(false);
        toast();
      });
  }
  return (
    <Center>
      <Box w="container.lg" borderRadius="2xl" borderWidth="1px" m="10" p="10">
        <Heading textAlign="center">Criar novo produto</Heading>
        <form onSubmit={submitCreate}>
          <FormControl>
            <FormLabel>Nome</FormLabel>
            <Input type="text" required name="name" />
          </FormControl>
          <FormControl>
            <FormLabel>Descrição</FormLabel>
            <Textarea name="description" />
          </FormControl>
          <FormControl>
            <FormLabel>Dimensões</FormLabel>
            <Textarea name="dimensions" />
          </FormControl>
          <FormControl>
            <FormLabel>Preço</FormLabel>
            <Input type="number" name="price" />
          </FormControl>
          <FormControl>
            <FormLabel>Imagens</FormLabel>
            <Input type="file" multiple name="images" />
          </FormControl>
          <Button
            type="submit"
            isLoading={loading}
            loadingText="Criando..."
            colorScheme="green"
            mt="5"
          >
            Criar
          </Button>
        </form>
      </Box>
    </Center>
  );
}
