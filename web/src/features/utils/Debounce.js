import{ useEffect, useState } from 'react';

export default function Debounce(value, delay) {
    const [debounceValue, setDebouceValue] = useState(value);

    useEffect(() => {
        const handler = setTimeout(() => {
            setDebouceValue(value);
        }, delay);

        // componentWillUnmount
        return () => {
            clearTimeout(handler);
        }
    }, [value]);

    return debounceValue;
}