package hska.iwi.eShopMaster.model.businessLogic.manager.impl;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import hska.iwi.eShopMaster.model.businessLogic.manager.CategoryManager;
import hska.iwi.eShopMaster.model.database.dataAccessObjects.CategoryDAO;
import hska.iwi.eShopMaster.model.database.dataobjects.Category;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.hc.client5.http.classic.methods.HttpDelete;
import org.apache.hc.client5.http.classic.methods.HttpGet;
import org.apache.hc.client5.http.classic.methods.HttpPost;
import org.apache.hc.client5.http.classic.methods.HttpUriRequestBase;
import org.apache.hc.client5.http.impl.classic.CloseableHttpClient;
import org.apache.hc.client5.http.impl.classic.CloseableHttpResponse;
import org.apache.hc.client5.http.impl.classic.HttpClients;
import org.apache.hc.core5.http.HttpEntity;
import org.apache.hc.core5.http.ParseException;
import org.apache.hc.core5.http.io.entity.EntityUtils;

public class CategoryManagerImpl implements CategoryManager{
	private ObjectMapper objectMapper;
	
	public CategoryManagerImpl() {
		objectMapper = new ObjectMapper();
	}

	public List<Category> getCategories() {
		List<Category> result = new ArrayList<Category>();
		try {
			HttpGet httpGet = new HttpGet(System.getenv("CATEGORY_SERVICE") + "/category");
			String responseString = executeRequest(httpGet);
			result = objectMapper.readValue(responseString, new TypeReference<List<Category>>(){});
			System.out.println(responseString);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
		return result;
	}

	public Category getCategory(int id) {
		Category result = null;
		try {
			HttpGet httpGet = new HttpGet(System.getenv("CATEGORY_SERVICE") + "/category/" + id);
			String responseString = executeRequest(httpGet);
			result = objectMapper.readValue(responseString, Category.class);
			System.out.println(responseString);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
		return result;
	}

	public Category getCategoryByName(String name) {
		Category result = null;
		try {
			HttpGet httpGet = new HttpGet(System.getenv("CATEGORY_SERVICE") + "/category?name=" + name);
			String responseString = executeRequest(httpGet);
			result = objectMapper.readValue(responseString, Category.class);
			System.out.println(responseString);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
		return result;
	}

	public void addCategory(String name) {
		try {
			HttpPost httpPost = new HttpPost(System.getenv("CATEGORY_SERVICE") + "/category?name=" + name);
			executeRequest(httpPost);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}

	public void delCategory(Category cat) {
		try {
			HttpDelete httpDelete = new HttpDelete(System.getenv("CATEGORY_SERVICE") + "/category/" + cat.getId());
			executeRequest(httpDelete);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}

	public void delCategoryById(int id) {
		try {
			HttpDelete httpDelete = new HttpDelete(System.getenv("CATEGORY_SERVICE") + "/category/" + id);
			executeRequest(httpDelete);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}


	private String executeRequest(HttpUriRequestBase httpMethod) throws IOException, ParseException {
		CloseableHttpClient httpClient = HttpClients.createDefault();
		CloseableHttpResponse response = httpClient.execute(httpMethod);
		HttpEntity entity = response.getEntity();
		String responseString = EntityUtils.toString(entity, "UTF-8");
		return responseString;
	}
}
