package service

import model.Person
import persistence.PersonRepository
import java.io.Serializable
import javax.faces.bean.ManagedBean
import javax.faces.bean.ViewScoped

@ManagedBean
@ViewScoped
class PersonService : Serializable {
    var id: Long = 0
    var firstName: String = ""
    var lastName: String = ""
    var age: Int = 0

    fun find(id: Long): Person? {
        return PersonRepository.find(id)
    }

    fun findAll(): List<Person> {
        return PersonRepository.findAll()
    }

    fun persist(item: Person): Boolean {
        return PersonRepository.persist(item)
    }

    fun add(): Boolean {
        val item = Person(null, lastName, firstName, age)

        firstName = ""
        lastName = ""
        age = 0

        return PersonRepository.persist(item)
    }

    fun add(item: Person): Boolean {
        return PersonRepository.persist(item)
    }

    fun add(firstName: String, lastName: String, age: Int): Boolean {
        return PersonRepository.persist(
                Person(null, firstName, lastName, age)
        )
    }

    fun update(): Boolean {
        val item = PersonRepository.find(id) ?: return false

        item.firstName = firstName
        item.lastName = lastName
        item.age = age

        id = 0
        firstName = ""
        lastName = ""
        age = 0

        return PersonRepository.merge(item)
    }

    fun update(item: Person): Boolean {
        return PersonRepository.merge(item)
    }

    fun update(id: Long, firstName: String?, lastName: String?, age: Int?): Boolean {
        val item = PersonRepository.find(id) ?: return false

        if (firstName != null) item.firstName = firstName
        if (lastName != null) item.firstName = lastName
        if (age != null) item.age = age

        return PersonRepository.merge(item)
    }
}