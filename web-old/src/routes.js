import welcome from './pages/Welcome'
import books from './pages/Books'

export default [
    {
        path: '/',
        name: 'welcome.page',
        component: welcome
    },
    { 
        path: '/books',
        name: 'books.page',
        component: books
    }
]