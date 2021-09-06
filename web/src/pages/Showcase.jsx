import React, { useContext, useEffect, useRef, useState } from 'react';
import {
  Box,
  Heading,
  Center,
  Image,
  Text,
  Badge,
  Button,
  AlertDialog,
  AlertDialogBody,
  AlertDialogHeader,
  AlertDialogFooter,
  AlertDialogContent,
  AlertDialogOverlay,
} from '@chakra-ui/react';
import { useHistory, useParams } from 'react-router';
import { deleteProduct, getSingleProduct } from '../services/productService';
import AppContext from '../context/appContext';

export default function Showcase() {
  const { id } = useParams();
  const [product, setProduct] = useState({});
  const { user } = useContext(AppContext);
  const [isOpen, setIsOpen] = useState(false);
  const cancelRef = useRef();
  const history = useHistory();

  function handleDelete() {
    setIsOpen(false);
    deleteProduct(product.id).then(() => {
      history.push('/');
    });
  }

  useEffect(() => {
    getSingleProduct(id)
      .then(response => {
        setProduct(response.data);
      })
      .catch(() => {});
  }, [id]);

  if (product.id) {
    return (
      <>
        <AlertDialog
          isOpen={isOpen}
          leastDestructiveRef={cancelRef}
          onClose={() => {
            setIsOpen(false);
          }}
          isCentered
        >
          <AlertDialogOverlay>
            <AlertDialogContent>
              <AlertDialogHeader fontSize="lg" fontWeight="bold">
                Deletar Produto
              </AlertDialogHeader>

              <AlertDialogBody>
                Tem certeza que deseja deletar o produto ? Essa ação não poderá
                ser desfeita!!
              </AlertDialogBody>

              <AlertDialogFooter>
                <Button
                  ref={cancelRef}
                  onClick={() => {
                    setIsOpen(false);
                  }}
                >
                  Cancelar
                </Button>
                <Button colorScheme="red" ml={3} onClick={handleDelete}>
                  Deletar
                </Button>
              </AlertDialogFooter>
            </AlertDialogContent>
          </AlertDialogOverlay>
        </AlertDialog>
        {product.owner.id === user.id ? (
          <Box
            w="full"
            h="14"
            bgColor="gray.100"
            d="flex"
            alignItems="center"
            justifyContent="flex-end"
            px="4"
            gridGap="4"
          >
            <Button colorScheme="blue">Editar</Button>
            <Button
              colorScheme="red"
              onClick={() => {
                setIsOpen(true);
              }}
            >
              Excluir
            </Button>
          </Box>
        ) : null}
        <Center>
          <Box width="container.lg" bgColor="blackAlpha.50" p={10}>
            <Heading>{product.name}</Heading>
            <Box d="flex" gridGap="4">
              {product.categories.map(category => {
                return (
                  <Badge key={category.id + category.name} mr={2}>
                    {category.name}
                  </Badge>
                );
              })}
              {product.owner.id === user.id ? (
                <Badge colorScheme="green">Adicionar Categoria</Badge>
              ) : null}
            </Box>
            <Box bgColor="#f2f2f2" my="4">
              <Image
                w="full"
                h="xl"
                objectFit="contain"
                src={product.images[0].path}
              />
            </Box>
            <Box d="flex" justifyContent="space-between" alignItems="center">
              <Heading as="h3" fontSize="3xl" fontWeight="300">
                Vendedor: {product.owner.username}
              </Heading>
              {product.price ? (
                <Heading as="h3" fontSize="3xl" fontWeight="300">
                  R$ {product.price}
                </Heading>
              ) : (
                <Text fontSize="lg" fontWeight="300">
                  Gratuíto
                </Text>
              )}
              <Button colorScheme="green">Comprar</Button>
            </Box>
            {product.description ? (
              <>
                <Heading size="md" my={4}>
                  Descrição
                </Heading>
                <Text>{product.description}</Text>
              </>
            ) : null}
            {product.dimensions ? (
              <>
                <Heading size="md" my={4}>
                  Dimensões
                </Heading>
                <Text>{product.dimensions}</Text>
              </>
            ) : null}
          </Box>
        </Center>
      </>
    );
  } else return null;
}
