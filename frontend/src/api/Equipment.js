import { getClient } from "./Config"

export const createEquipmentsAPI = async (data) => {
    return await getClient().post("/equipment/", data);
}