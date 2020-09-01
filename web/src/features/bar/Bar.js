import React, { useEffect, useState } from 'react';
import { useDispatch } from 'react-redux';
import { makeStyles, fade } from '@material-ui/core/styles';
import { 
    AppBar,
    Typography,
    InputBase,
    Toolbar
} from '@material-ui/core';
import useDebounce from '../utils/Debounce';
import { 
    searchAsync,
} from '../books/booksSlice';

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
    },
    title: {
        flexGrow: 1,
        display: 'none',
        [theme.breakpoints.up('sm')]: {
          display: 'block',
        },
    },
    search: {
        position: 'relative',
        borderRadius: theme.shape.borderRadius,
        backgroundColor: fade(theme.palette.common.white, 0.15),
        '&:hover': {
          backgroundColor: fade(theme.palette.common.white, 0.25),
        },
        marginLeft: 0,
        width: '100%',
        [theme.breakpoints.up('sm')]: {
          marginLeft: theme.spacing(1),
          width: 'auto',
        },
    },
    inputRoot: {
        color: 'inherit',
    },
    inputInput: {
        padding: theme.spacing(1, 1, 1, 0),
        paddingLeft: `calc(1em + ${theme.spacing(4)}px)`,
        transition: theme.transitions.create('width'),
        width: '100%',
        [theme.breakpoints.up('sm')]: {
            width: '12ch',
            '&:focus': {
            width: '20ch',
            },
        },
    },
}));

export function Bar() {
    const classes = useStyles();
    const dispatch = useDispatch();

    // especificamos el hook correspondiente al texto de búsqueda, utilizaremos hook en onChange de input base.
    const [searchTerm, setSearchTem] = useState('');
    const debounceSearchValue = useDebounce(searchTerm, 500);

    useEffect(() => {
        const filters = { search: debounceSearchValue || '' };
        dispatch(searchAsync(filters));
    }, [debounceSearchValue]); // especificamos debouncesearchvalue para rastrear estado, en caso contrario, actualización seria infinita.

    return (
        <div className={classes.root}>
            <AppBar position="static">
                <Toolbar>
                    <Typography className={classes.title} noWrap>
                        Aukoo - ReactJS
                    </Typography>
                    <div className={classes.search}>
                        <InputBase
                            placeholder='Buscar'
                            onChange={(e) => setSearchTem(e.target.value) }
                            classes={{
                                root: classes.inputRoot,
                                input: classes.inputInput,
                            }}>
                        </InputBase>
                    </div>
                </Toolbar>
            </AppBar>
        </div>
    )
}