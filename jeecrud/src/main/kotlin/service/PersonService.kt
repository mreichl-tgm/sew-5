package service

import model.Person
import persistence.PersonRepository
import java.io.Serializable
import javax.faces.bean.ManagedBean

@ManagedBean
class PersonService : Serializable {
    var id: Long = 0
    var firstName: String = ""
    var lastName: String = ""
    var age: Int = 0

    fun find(): Person? {
        return PersonRepository.find(id)
    }

    fun find(id: Long): Person? {
        return PersonRepository.find(id)
    }

    fun findAll(): List<Person> {
        return PersonRepository.findAll()
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

        if (firstName != "") item.firstName = firstName
        if (lastName != "") item.lastName = lastName
        if (age > 0) item.age = age

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

    fun remove(): Boolean {
        return PersonRepository.remove(id)
    }
}