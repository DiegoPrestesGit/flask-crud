package college.crud.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

import college.crud.exception.ResourceNotFoundException;
import college.crud.models.User;
import college.crud.repositories.UsersRepository;

@RestController
@RequestMapping("api/java")
public class UserController {
	@Autowired
	private UsersRepository usersRepository;

	@GetMapping("users")
	public List<User> getAllUsers() {
		return this.usersRepository.findAll();
	}

	@GetMapping("users/{id}")
	public ResponseEntity<User> getUserById(@PathVariable(value = "id") String userId)
			throws ResourceNotFoundException {
		User user = usersRepository.findById(userId)
				.orElseThrow(() -> new ResourceNotFoundException("User not found with the id: " + userId));
		return ResponseEntity.ok().body(user);
	}

	@PostMapping("users")
	public User createUser(@Validated @RequestBody User user) {
		return this.usersRepository.save(user);
	}
}
