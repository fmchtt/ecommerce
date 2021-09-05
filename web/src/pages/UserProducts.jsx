import React, { useEffect, useState } from 'react';
import {
  Box,
  Grid,
  GridItem,
  Image,
  Badge,
  LinkBox,
  Center,
  Button,
} from '@chakra-ui/react';
import { Link } from 'react-router-dom';
import { getProductsOfUser } from '../services/productService';

export default function CreatedByUser() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    getProductsOfUser().then(response => {
      setProducts(response.data);
    });
  }, []);

  return (
    <>
      <Box w="full" h="14" bgColor="gray.100" d="flex" alignItems="center" justifyContent="flex-end" pr="4">
        <Button colorScheme="green" as={Link} to="/products/create">Criar novo</Button>
      </Box>
      <Center>
        <Grid
          padding="5"
          templateColumns="repeat(5, 1fr)"
          w="container.md"
          gap={5}
        >
          {products.map(product => {
            return (
              <GridItem key={product.id} borderWidth="1px" borderRadius="lg">
                <LinkBox as={Link} to={`/product/${product.id}`}>
                  <Box w="full">
                    <Box>
                      <Image
                        p="2"
                        w="full"
                        h="xs"
                        objectFit="cover"
                        src={product.images[0].path}
                      />
                    </Box>
                    <Box p="6">
                      <Box d="flex">
                        {product.categories.map(category => {
                          return (
                            <Badge mr="2" key={category.id + category.name}>
                              {category.name}
                            </Badge>
                          );
                        })}
                      </Box>
                      <Box mt="1" fontWeight="semibold" as="h4" isTruncated>
                        {product.name}
                      </Box>
                      <Box>R$ {product.price.toFixed(2)}</Box>
                    </Box>
                  </Box>
                </LinkBox>
              </GridItem>
            );
          })}
        </Grid>
      </Center>
    </>
  );
}
