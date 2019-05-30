<template>
    <div>
        <div class="row">
            <div class="col col-xs-12">
                <h3>
                    <small><a href="http://books.toscrape.com" target="_blank">http://books.toscrape.com</a></small>
                </h3>
            </div>
        </div>
        <div class="row">
            <div class="col col-sm-6">
                <div class="input-group">
                    <input type="text" class="form-control form-control-sm" v-model="filters.query" placeholder="Busca por titulo" aria-describedby="basic-addon2">
                    <div class="input-group-append">
                        <button class="btn btn-primary btn-sm" type="button" @click="search">Buscar</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col col-sm-12" style="margin-top:5px;">
                <div style="border: 0.5px solid #ddd; padding: 9px; border-radius:4px;">
                    <select name="" id="" class="form-control form-control-sm" style="width: 60% !important;" v-model="filters.category" v-if="categories_list && categories_list.length">
                        <option value="-1" selected>Seleccione una categoria</option>
                        <option v-for="(category, index) in categories_list" :key="index" :value="category.id">
                            {{ category.name }}
                        </option>
                    </select>
                </div>
            </div>
        </div>
        <br>
        <div class="row">
            <div class="col col-xs-12">
                <v-server-table ref="books"
                    id="books"
                    :css="table.css"
                    :url="''"
                    :columns="table.columns"
                    :options="table.options"
                    pagination-path="">
                    <a :href="props.row.category.url" slot="category" slot-scope="props" target="_blank">{{ props.row.category.name }}</a>
                    <ul slot="actions" slot-scope="props" class="list-inline">
                        <li class="list-inline-item"><button class="btn btn-danger btn-sm" @click="removeBook(props.row.id)">Eliminar</button></li>
                    </ul>
                </v-server-table>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
      return {
        filters: {
           query: '',
           category: -1
        },
        categories_list: [],
        table: {
            apiMode: true,
            columns: [
                'id',
                'title',
                'category',
                'price',
                'tax',
                'upc',
                'actions'
            ],
            options: {
                requestFunction: this.searchBooks,
                responseAdapter: this.searchBooksTransform,
                perPageValues: [5],
                filterable: false,
                perPage: 5,
                skin: 'table table-sm table-striped',
                sortable: ['id', 'title', 'price'],
                headings: {
                    id: 'ID',
                    title: 'Titulo',
                    category: 'Categoria',
                    price: 'Precio',
                    tax: 'Impuesto',
                    upc: 'UPC',
                    actions: ''
                },
                texts: {
                    filterPlaceholder: 'Búsqueda ',
                    filter: 'Resultado de filtros:',
                    count: 'Mostrando {from} de {count} registros',
                    page: 'Página:',
                    noResults: 'No se han encontrado registros',
                    loading: 'Cargando...',
                    defaultOption: 'Seleccione {column}',
                },
            },
        },
      }
    },
    created() {
        this.loadCategories()
    },
    methods: {
        search() {
           this.$refs.books.refresh()
        },
        removeBook(bookId) {
            this.axios.delete(`api/v1/books/${bookId}/delete`).then((response) => {
               let data = response.data;
               if (data.success === true) {
                   this.search()
               }
               else {
                   alert('Ha ocurrido un error al procesar su solicitud.')
               }
            })
        },
        searchBooks(criteria) {
           criteria.categoryId = this.filters.category
           criteria.query = this.filters.query
           return this.axios.post('api/v1/books/search', criteria).then((response) => {
               return response.data
           }).catch(() => {
               console.log(err);
           });
        },
        searchBooksTransform(data) {
           return data;
        },
        loadCategories() {
            this.axios.get('api/v1/categories').then((response) => {
                this.categories_list = response.data;
            })
        },
    },
}
</script>

<style lang="scss" scoped>

</style>