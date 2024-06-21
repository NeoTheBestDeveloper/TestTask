import { getClient, getUnauthorizedClient, setToken, deleteToken } from './config';

export const loginAPI = async (username, password) => {
    const response = await getUnauthorizedClient().post("/user/login/", { username, password });

    setToken(response.data.data);

    return response;
}

export const registerAPI = async (username, email, password) => {
    return await getUnauthorizedClient().post('/user/', { username, email, password });
}

export const logoutAPI = async () => {
    const result = await getClient().post('/user/logout/');
    deleteToken();
    return result;
}