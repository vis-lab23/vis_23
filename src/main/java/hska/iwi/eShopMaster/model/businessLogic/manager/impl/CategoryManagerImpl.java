package hska.iwi.eShopMaster.model.businessLogic.manager.impl;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import hska.iwi.eShopMaster.model.businessLogic.manager.CategoryManager;
import hska.iwi.eShopMaster.model.database.dataAccessObjects.CategoryDAO;
import hska.iwi.eShopMaster.model.database.dataobjects.Category;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.List;

public class CategoryManagerImpl implements CategoryManager{
	private CategoryDAO helper;
	private HttpClient client;
	private ObjectMapper objectMapper;
	
	public CategoryManagerImpl() {
		helper = new CategoryDAO();
		helper = new CategoryDAO();
		client = HttpClient.newHttpClient();
		objectMapper = new ObjectMapper();
	}

	public List<Category> getCategories() {
		HttpRequest request;
		try {
			request = HttpRequest.newBuilder()
					.uri(new URI("http://cattegory-servcie:3000/category"))
					.GET()
					.build();
			HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
			String body = response.body();
			return objectMapper.readValue(body, new TypeReference<List<Category>>(){});
		} catch (URISyntaxException e) {
			throw new RuntimeException(e);
		} catch (IOException e) {
			throw new RuntimeException(e);
		} catch (InterruptedException e) {
			throw new RuntimeException(e);
		}
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
