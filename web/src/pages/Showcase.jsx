import React, { useEffect, useState } from 'react';
import {
  Box,
  Heading,
  Center,
  Image,
  Text,
  Badge,
  Button
} from '@chakra-ui/react';
import { useParams } from 'react-router';
import { getSingleProduct } from '../services/productService';

export default function Showcase() {
  const { id } = useParams();
  const [product, setProduct] = useState({});

  useEffect(() => {
    getSingleProduct(id)
      .then(response => {
        setProduct(response.data);
      })
      .catch(() => {});
  }, [id]);

  if (product.id) {
    return (
      <Center mt={10}>
        <Box width="container.lg">
          <Heading>{product.name}</Heading>
          {product.categories.map(category => {
            return <Badge mr={2}>{category.name}</Badge>;
          })}
          <Box bgColor="#f2f2f2" my="4">
            <Image
              w="full"
              h="xl"
              objectFit="contain"
              src={product.images[0].path}
            />
          </Box>
          <Box d="flex" justifyContent="space-between" alignItems="center">
            {product.price ? (
              <Text fontSize="lg" fontWeight="300">
                Valor: R$ {product.price}
              </Text>
            ) : (
              <Text fontSize="lg" fontWeight="300">
                Gratuíto
              </Text>
            )}
            <Button colorScheme="green">Comprar</Button>
          </Box>
          {product.description ? (
            <>
              <Heading size="md" my={4}>Descrição</Heading>
              <Text>{product.description}</Text>
            </>
          ) : null}
          {product.dimensions ? (
            <>
              <Heading size="md" my={4}>Dimensões</Heading>
              <Text>{product.dimensions}</Text>
            </>
          ) : null}
        </Box>
      </Center>
    );
  } else return null;
}
