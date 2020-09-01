import { createSlice } from '@reduxjs/toolkit';

export const booksSlice = createSlice({
  name: 'books',
  initialState: {
    loading: false,
    books: {
      data: [],
      count: 0,
    },
  },
  reducers: {
    loading: (state, { payload }) => {
      state.loading = payload;
    },
    search: (state, { payload }) => { // mutación
      if (payload) {
        state.books.data = payload.data;
        state.books.count = payload.count;
      }
    },
  },
});

export const { search, loading } = booksSlice.actions;

export const searchAsync = filters => async dispatch => { // acción
  // TODO: axios;
  dispatch(loading(true));
  setTimeout(() => {
    const payload = { data: [{ Id: 1, Name: 'Carlos', Category: 'Comedia', Ranking: 5 }], count: 1 };
    dispatch(search(payload));
    dispatch(loading(false));
  }, 1000);
};

export const selectSearch = state => state.books.books; // getter
export const selectSearchLoading = state => state.books.loading;

export default booksSlice.reducer;