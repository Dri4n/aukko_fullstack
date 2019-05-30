import welcome from './pages/Welcome'
import categories from './pages/Categories'
import books from './pages/Books'

export default [
    {
        path: '/',
        name: 'welcome.page',
        component: welcome
    },
    { 
        path: '/categories',
        name: 'categories.page',
        component: categories
    },
    { 
        path: '/books',
        name: 'books.page',
        component: books
    }
]