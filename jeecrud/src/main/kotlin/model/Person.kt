package model

import javax.persistence.Entity
import javax.persistence.GeneratedValue
import javax.persistence.Id

@Entity
data class Person(@Id @GeneratedValue var id: Long?, var lastName: String, var firstName: String, var age: Int) {
    override fun toString(): String {
        return firstName + " " + lastName
    }
}