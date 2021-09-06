import React, { useContext, useEffect, useState } from 'react';
import {
  Box,
  Grid,
  GridItem,
  Image,
  Badge,
  LinkBox,
  Heading,
  Button,
  Flex,
} from '@chakra-ui/react';
import { getProducts } from '../services/productService';
import { Link } from 'react-router-dom';
import AppContext from '../context/appContext';

export default function Home() {
  const [products, setProducts] = useState([]);
  const { categories } = useContext(AppContext);

  useEffect(() => {
    getProducts().then(response => {
      setProducts(response.data);
    });
  }, []);

  return (
    <Box as="main" padding="5">
      <Heading textAlign="center" fontWeight="300" pb="5">
        Ultimos produtos adicionados para a venda!
      </Heading>
      <Grid templateColumns="repeat(6, 1fr)" w="full" gap={5}>
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
      <Heading textAlign="center" fontWeight="300" py="5">
        Veja nossos produtos pela categoria que procura!!
      </Heading>
      <Flex padding="5" w="full" gridGap={5} justifyContent="center">
        {categories.map(category => {
          return (
            <Button key={category.id + category.name}>{category.name}</Button>
          );
        })}
      </Flex>
    </Box>
  );
}
