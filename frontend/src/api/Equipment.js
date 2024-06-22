import { getClient } from "./Config"

export const createEquipmentsAPI = async (data) => {
    return await getClient().post("/equipment/", data);
}

export const fetchEquipmentsAPI = async (page, filterBy, filterByCriteria) => {
    return await getClient().get(`/equipment/?page=${page}&${filterBy}=${filterByCriteria}`);
}