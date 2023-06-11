package hska.iwi.eShopMaster.model.businessLogic.manager.impl;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

import hska.iwi.eShopMaster.model.businessLogic.manager.CategoryManager;
import hska.iwi.eShopMaster.model.businessLogic.manager.ProductManager;
import hska.iwi.eShopMaster.model.database.dataAccessObjects.ProductDAO;
import hska.iwi.eShopMaster.model.database.dataobjects.Category;
import hska.iwi.eShopMaster.model.database.dataobjects.Product;

import org.apache.hc.client5.http.classic.methods.HttpDelete;
import org.apache.hc.client5.http.classic.methods.HttpGet;
import org.apache.hc.client5.http.classic.methods.HttpPost;
import org.apache.hc.client5.http.classic.methods.HttpUriRequestBase;
import org.apache.hc.client5.http.impl.classic.CloseableHttpClient;
import org.apache.hc.client5.http.impl.classic.CloseableHttpResponse;
import org.apache.hc.client5.http.impl.classic.HttpClients;
import org.apache.hc.core5.http.ContentType;
import org.apache.hc.core5.http.HttpEntity;
import org.apache.hc.core5.http.ParseException;
import org.apache.hc.core5.http.io.entity.EntityUtils;
import org.apache.hc.core5.http.io.entity.StringEntity;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

public class ProductManagerImpl implements ProductManager {
	private ObjectMapper objectMapper;
	private TypeReference<List<Product>> typeReference;
	
	public ProductManagerImpl() {
		objectMapper = new ObjectMapper();
		typeReference = new TypeReference<List<Product>>(){};
	}

	public List<Product> getProducts() {
		List<Product> result = new ArrayList<Product>();
		try {
			HttpGet httpGet = new HttpGet(System.getenv("PRODUCT_SERVICE") + "/products");
			String responseString = executeRequest(httpGet);
			result = objectMapper.readValue(responseString, typeReference);
			System.out.println(responseString);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
		return result;
	}
	
	public List<Product> getProductsForSearchValues(String searchDescription,
		Double searchMinPrice, Double searchMaxPrice) {
		List<Product> result = new ArrayList<Product>();
		try {
			HttpGet httpGet = new HttpGet(
				System.getenv("PRODUCT_SERVICE") + 
				"/products?search=" + searchDescription +
				"&min_price=" + searchMinPrice +
				"&max_price=" + searchMaxPrice
			);
			String responseString = executeRequest(httpGet);
			result = objectMapper.readValue(responseString, typeReference);
			System.out.println(responseString);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
		return result;
	}

	public Product getProductById(int id) {
		Product result = null;
		try {
			HttpGet httpGet = new HttpGet(
				System.getenv("PRODUCT_SERVICE") + "/products/" + id + "/");
			String responseString = executeRequest(httpGet);
			result = objectMapper.readValue(responseString, Product.class);
			System.out.println(responseString);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
		return result;
	}

	public Product getProductByName(String name) {
		Product result = null;
		try {
			HttpGet httpGet = new HttpGet(
				System.getenv("PRODUCT_SERVICE") + "/products/" + name + "/");
			String responseString = executeRequest(httpGet);
			result = objectMapper.readValue(responseString, Product.class);
			System.out.println(responseString);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
		return result;
	}
	
	public int addProduct(String name, double price, String categoryName, String details) {
		try {
			HttpPost httpPost = new HttpPost(System.getenv("PRODUCT_SERVICE") + "/products/");
			
			StringEntity entity = new StringEntity(
				"{\"name\": \"" + name + 
				"\",\"details\": \"" + details +
				"\",\"price\": \"" + price +
				"\",\"category\": \"" + categoryName + "\"}",
				ContentType.create("application/json", StandardCharsets.UTF_8)
			);
			
			httpPost.setEntity(entity);
    		httpPost.setHeader("Accept", "application/json");
    		httpPost.setHeader("Content-type", "application/json");
			String responseString = executeRequest(httpPost);
			System.out.println(responseString);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
		return 1;
	}
	

	public void deleteProductById(int id) {
		System.out.println("bruh");
		try {
			HttpDelete httpDelete = new HttpDelete(System.getenv("PRODUCT_SERVICE") + "/products/" + id + "/");
			String responseString = executeRequest(httpDelete);
			System.out.println(responseString);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}

	public boolean deleteProductsByCategoryId(int categoryId) {
		// TODO Auto-generated method stub
		return false;
	}
	
	private String executeRequest(HttpUriRequestBase httpMethod) throws IOException, ParseException {
		CloseableHttpClient httpClient = HttpClients.createDefault();
		CloseableHttpResponse response = httpClient.execute(httpMethod);
		HttpEntity entity = response.getEntity();
		String responseString = EntityUtils.toString(entity, "UTF-8");
		return responseString;
	}
}
