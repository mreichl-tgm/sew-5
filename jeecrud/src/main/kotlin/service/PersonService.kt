package service

import model.Person
import persistence.PersonRepository
import java.io.Serializable
import javax.faces.bean.ManagedBean

@ManagedBean
class PersonService : Serializable {
    fun find(id: Long): Person? {
        return PersonRepository.find(id)
    }

    fun findAll(): List<Person> {
        return PersonRepository.findAll()
    }
}