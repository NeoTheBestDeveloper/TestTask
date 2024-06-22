import { getClient } from "./Config"

export const createEquipmentsAPI = async (data) => {
    return await getClient().post("/equipment/", data);
}

export const fetchEquipmentsAPI = async (page, filterByKey, filterByValue) => {
    return await getClient().get(`/equipment/?page=${page}&${filterByKey}=${filterByValue}`);
}

export const deleteEquipmentAPI = async (id) => {
    return await getClient().delete(`/equipment/${id}/`)
}