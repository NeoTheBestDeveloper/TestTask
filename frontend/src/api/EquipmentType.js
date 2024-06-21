import { getClient } from './Config';

export const fetchTypesAPI = async () => {
    return (await getClient().get('/equipment-type/')).data;
}