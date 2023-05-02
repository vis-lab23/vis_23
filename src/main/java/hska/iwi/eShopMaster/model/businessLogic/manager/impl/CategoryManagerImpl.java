package hska.iwi.eShopMaster.model.businessLogic.manager.impl;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import hska.iwi.eShopMaster.model.businessLogic.manager.CategoryManager;
import hska.iwi.eShopMaster.model.database.dataAccessObjects.CategoryDAO;
import hska.iwi.eShopMaster.model.database.dataobjects.Category;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.hc.client5.http.classic.methods.HttpGet;
import org.apache.hc.client5.http.impl.classic.CloseableHttpClient;
import org.apache.hc.client5.http.impl.classic.CloseableHttpResponse;
import org.apache.hc.client5.http.impl.classic.HttpClients;

public class CategoryManagerImpl implements CategoryManager{
	private CategoryDAO helper;
	private ObjectMapper objectMapper;
	
	public CategoryManagerImpl() {
		helper = new CategoryDAO();
		helper = new CategoryDAO();
		objectMapper = new ObjectMapper();
	}

	public List<Category> getCategories() {
		List<Category> result = new ArrayList<Category>();
		try {
			HttpGet httpGet = new HttpGet("http://category-service:3000/category");
			CloseableHttpClient httpClient = HttpClients.createDefault();
			CloseableHttpResponse response = httpClient.execute(httpGet);
			String body = response.getEntity().toString();

			result = objectMapper.readValue(body, new TypeReference<List<Category>>(){});
		} catch (Exception e) {}
		return result;
	}

	public Category getCategory(int id) {
		return helper.getObjectById(id);
	}

	public Category getCategoryByName(String name) {
		return helper.getObjectByName(name);
	}

	public void addCategory(String name) {
		Category cat = new Category(name);
		helper.saveObject(cat);

	}

	public void delCategory(Category cat) {
	
// 		Products are also deleted because of relation in Category.java 
		helper.deleteById(cat.getId());
	}

	public void delCategoryById(int id) {
		
		helper.deleteById(id);
	}
}
