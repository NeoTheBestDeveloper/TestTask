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

export const editEquipmentAPI = async (id, serial_number, type_id, description) => {
    return await getClient().put(`/equipment/${id}/`, { serial_number, type_id, description });
}