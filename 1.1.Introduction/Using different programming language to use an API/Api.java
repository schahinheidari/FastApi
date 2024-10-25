import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class Api {

    private static String sendGetRequest(String urlString) throws Exception {
        URL url = new URL(urlString);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");
        connection.setRequestProperty("User-Agent", "Mozilla/5.0");

        int responseCode = connection.getResponseCode();
        if (responseCode == HttpURLConnection.HTTP_OK) {
            BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            String inputLine;
            StringBuilder response = new StringBuilder();

            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();
            return response.toString();
        } else {
            return "GET request failed with response code: " + responseCode;
        }
    }

    public static void main(String[] args) {
        try {
            // First API request (number_api)
            String numberApi = "http://numbersapi.com/13";
            String numberApiResponse = sendGetRequest(numberApi);
            System.out.println("number_api: " + numberApiResponse);

            // Second API request (harryPotter-api)
            String hpApi = "https://hp-api.onrender.com/api/characters";
            String hpApiResponse = sendGetRequest(hpApi);
            System.out.println("hp-api: " + hpApiResponse);

            // Third API request (weather_api)
            String weatherApi = "https://goweather.herokuapp.com/weather/Sarkhon";
            String weatherApiResponse = sendGetRequest(weatherApi);
            System.out.println("weather_api: " + weatherApiResponse);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
