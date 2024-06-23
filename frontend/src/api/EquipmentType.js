import { getClient } from './Config';

export const fetchTypesAPI = async () => {
    let response = await getClient().get('/equipment-type/');
    return response.data.data.flatMap((item) => {
        return {
            id: item.id,
            title: item.name,
            serial_number_mask: item.serial_number_mask,
        }
    })
}