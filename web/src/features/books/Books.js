import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {
  searchAsync,
  selectSearch,
  selectSearchLoading,
} from './booksSlice';
import {
    Paper,
    TableContainer,
    Table,
    TableHead,
    TableBody,
    TableRow,
    TableCell
} from '@material-ui/core';

function renderBooks(loadingBooks, books) {
  if (loadingBooks === true) {
    return (
      <TableRow key={0}>
        <TableCell>Cargando...</TableCell>
      </TableRow>
    );
  }
  
  const rows = books.data;
  const data = (row) => (
    <TableRow key={row.Id}>
        <TableCell>{row.Id}</TableCell>
        <TableCell>{row.Name}</TableCell>
        <TableCell>{row.Category}</TableCell>
        <TableCell>{row.Ranking}</TableCell>
    </TableRow>
  )

  return rows.map((book) => data(book));
}

export function Books() {
  const books = useSelector(selectSearch);
  const loadingBooks = useSelector(selectSearchLoading);

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(searchAsync({}));
  }, [dispatch]);

  return (
    <TableContainer component={Paper}>
        <Table aria-label="listado de libros - scraping">
            <TableHead>
                <TableRow>
                    <TableCell>ID</TableCell>
                    <TableCell>Nombre</TableCell>
                    <TableCell>Categoría</TableCell>
                    <TableCell>Ranking</TableCell>
                </TableRow>
            </TableHead>
            <TableBody>
              {renderBooks(loadingBooks, books)}
            </TableBody>
        </Table>
    </TableContainer>
  );
}