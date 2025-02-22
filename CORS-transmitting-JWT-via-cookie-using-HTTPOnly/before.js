const axios = require("axios");

const getUserProfile = async (token) => {
  try {
    const response = await axios.get("http://fast-api:8000/api/profile", {
      withCredentials: true, // Send cookies with the request
    });
    return response.data;
  } catch (error) {
    console.error("Error fetching user profile:", error);

    if (error.response) {
      console.error("Response error data:", error.response.data);
      console.error("Response error status:", error.response.status);
      console.error("Response error headers:", error.response.headers);
    } else if (error.request) {
      console.error("Request error data:", error.request);
    } else {
      console.error("General error message:", error.message);
    }

    throw new Error("Failed to fetch user profile");
  }
};
