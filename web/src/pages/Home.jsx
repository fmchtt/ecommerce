import React, { useEffect, useState } from 'react';
import {
  Box,
  Grid,
  GridItem,
  Image,
  Badge,
  LinkBox,
  Center,
} from '@chakra-ui/react';
import { getProducts } from '../services/productService';
import { Link } from 'react-router-dom';

export default function Home() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    getProducts().then(response => {
      setProducts(response.data);
    });
  }, []);

  return (
    <Center>
      <Grid
        padding="5"
        templateColumns="repeat(4, 1fr)"
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
  );
}
