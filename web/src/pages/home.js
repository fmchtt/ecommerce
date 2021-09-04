import React, { useEffect, useState } from 'react';
import { Box, Grid, GridItem, Image, Badge } from '@chakra-ui/react';
import { getProducts } from '../services/productService';

export default function Home() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    getProducts().then(response => {
      setProducts(response.data);
    });
  }, []);

  return (
    <Box w="full">
      <Grid padding="5" templateColumns="repeat(5, 1fr)" gap={5}>
        {products.map(product => {
          return (
            <GridItem key={product.id} borderWidth="1px" borderRadius="lg">
              <Box w="full">
                <Box>
                  <Image p="2" width="full" maxH="xs" objectFit="cover" src={product.images[0].path} />
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
            </GridItem>
          );
        })}
      </Grid>
    </Box>
  );
}
