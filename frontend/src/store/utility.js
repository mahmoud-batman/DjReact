export const updateObject = (oldObject, updatedProperties) => {
  return {
    ...oldObject,
    ...updatedProperties,
  };
};

export const authurl = "http://127.0.0.1:8000/api/v1/users/rest-auth";
