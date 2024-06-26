import axios from 'axios'

const baseURL = 'http://localhost/api';

export const getToken = () => {
    return localStorage.getItem('token');
}

export const setToken = (token) => {
    localStorage.setItem('token', token);
}

export const deleteToken = () => {
    localStorage.clear('token');
}

export const getClient = () => {
    return axios.create({
        baseURL: baseURL,
        headers: {
            'Authorization': `Bearer ${getToken()}`,
        },
    });
};

export const getUnauthorizedClient = () => {
    return axios.create({
        baseURL: baseURL,
    });
};