package service

import model.Person
import persistence.PersonRepository
import java.io.Serializable
import javax.faces.bean.ManagedBean


/**
 * @author Markus Reichl
 * @version 05.10.2017
 *
 * Service bean providing an interface to the PersonRepository
 */
@ManagedBean
class PersonService : Serializable {
    var id: Long = 0
    var firstName: String = ""
    var lastName: String = ""
    var age: Int = 0

    /**
     * Returns the Person Entity instance if it matches the current id
     * @return Person object using the current id or null
     */
    fun find(): Person? {
        return PersonRepository.find(id)
    }

    /**
     * Returns the person with the given id
     * @return Person with the given id
     */
    fun find(id: Long): Person? {
        return PersonRepository.find(id)
    }

    /**
     * Returns all Person Entity instances found in the database
     * @return List of all persons
     */
    fun findAll(): List<Person> {
        return PersonRepository.findAll()
    }

    /**
     * Adds a new Person to the database using the lastName, firstName and age variables
     * @return true on success else false
     */
    fun add(): Boolean {
        val item = Person(null, lastName, firstName, age)

        firstName = ""
        lastName = ""
        age = 0

        return PersonRepository.persist(item)
    }

    /**
     * Adds the given person to the database
     * @return true on success else false
     */
    fun add(item: Person): Boolean {
        return PersonRepository.persist(item)
    }

    /**
     * Adds a new Person to the database using the given lastName, firstName and age values
     * @return true on success else false
     */
    fun add(firstName: String, lastName: String, age: Int): Boolean {
        return PersonRepository.persist(
                Person(null, firstName, lastName, age)
        )
    }

    /**
     * Updates a matching person using the id, lastName, firstName and age variables
     * @return true on success else false
     */
    fun update(): Boolean {
        val item = PersonRepository.find(id) ?: return false

        if (firstName != "") item.firstName = firstName
        if (lastName != "") item.lastName = lastName
        if (age > 0) item.age = age

        return PersonRepository.merge(item)
    }

    /**
     * Updates the given person
     * @return true on success else false
     */
    fun update(item: Person): Boolean {
        return PersonRepository.merge(item)
    }

    /**
     * Updates a matching person using the given id, lastName, firstName and age values
     * @return true on success else false
     */
    fun update(id: Long, firstName: String?, lastName: String?, age: Int?): Boolean {
        val item = PersonRepository.find(id) ?: return false

        if (firstName != null) item.firstName = firstName
        if (lastName != null) item.firstName = lastName
        if (age != null) item.age = age

        return PersonRepository.merge(item)
    }

    /**
     * Deletes the person with the given id
     * @return true on success else false
     */
    fun remove(): Boolean {
        return PersonRepository.remove(id)
    }
}